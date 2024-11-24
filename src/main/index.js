import { app, shell, BrowserWindow, ipcMain, dialog } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import { get_token, getAlbum, getArtistTopTrack, getTrack, search } from './spotify_api.js'
import { download } from './spotdl.js'

function createWindow() {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 1100,
    height: 618,
    minWidth: 500,
    minHeight: 400,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow.show()
  })

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    mainWindow.loadFile(join(__dirname, '../renderer/index.html'))
  }
}

app.whenReady().then(() => {
  // Set app user model id for windows
  electronApp.setAppUserModelId('com.github.Didiloy')

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  // IPC
  ipcMain.on('get-token', async () => {
    const results = await get_token()
    BrowserWindow.getFocusedWindow().webContents.send('get-token', results)
  })

  ipcMain.on('search', async (event, query) => {
    const results = await search(query)
    BrowserWindow.getFocusedWindow().webContents.send('search_result', results)
  })

  ipcMain.on('search_album', async (event, query) => {
    const results = await getAlbum(query)
    BrowserWindow.getFocusedWindow().webContents.send('search_album_result', results)
  })

  ipcMain.on('search_track', async (event, query) => {
    const results = await getTrack(query)
    BrowserWindow.getFocusedWindow().webContents.send('search_track_result', results)
  })

  ipcMain.on('search_artist', async (event, query) => {
    const results = await getArtistTopTrack(query)
    BrowserWindow.getFocusedWindow().webContents.send('search_artist_result', results)
  })

  ipcMain.on('download', async (event, query) => {
    download(query.link, query.path, query.format, query.bitrate, query.songs_to_delete)
  })

  ipcMain.on('open-link', (event, url) => {
    event.preventDefault()
    shell.openExternal(url)
  })

  ipcMain.on('select-directory', () => {
    const directory = selectDirectory()
    BrowserWindow.getAllWindows()[0].webContents.send('selected-directory', directory[0])
  })

  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

function selectDirectory() {
  const result = dialog.showOpenDialogSync(BrowserWindow.getFocusedWindow(), {
    properties: ['openDirectory']
  })
  return result
}
