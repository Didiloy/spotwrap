import { execFile } from 'child_process'
import { unlink } from 'node:fs'
import { BrowserWindow } from 'electron'
import spotdl from '../../resources/bin/spotdl?asset&asarUnpack'
const FILENAME_FORMAT = '{artist} - {title}.{output-ext}'

export function download(link, output_path, format, bitrate, song_to_delete) {
  const args = [
    link,
    '--bitrate',
    bitrate,
    '--format',
    format,
    '--print-errors',
    '--output',
    output_path !== '' ? output_path + '/' + FILENAME_FORMAT : FILENAME_FORMAT
  ]
  const child = execFile(spotdl, args, { windowsHide: true }, (error, stdout, stderr) => {
    if (error) {
      console.log(error)
    }
    if (song_to_delete.length > 0) {
      for (const song of song_to_delete) {
        const path = output_path + '/' + song + '.' + format
        unlink(path, (err) => {
          if (err) {
            console.log('could not delete song ' + song)
            BrowserWindow.getAllWindows()[0].webContents.send(
              'update_in_download',
              'could not delete song ' + song
            )
            return
          }
          console.log(path + ' was deleted')
          BrowserWindow.getAllWindows()[0].webContents.send(
            'update_in_download',
            path + ' was deleted'
          )
        })
      }
    }
    BrowserWindow.getAllWindows()[0].webContents.send('update_in_download', 'Done')
  })

  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`)
    BrowserWindow.getAllWindows()[0].webContents.send('update_in_download', data)
  })
}
