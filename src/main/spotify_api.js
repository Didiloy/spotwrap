import axios from 'axios'
import 'dotenv/config'
import { BrowserWindow } from 'electron'
const TOKEN_URL = 'https://accounts.spotify.com/api/token'
const BASE_URL = 'https://api.spotify.com/v1'
const SEARCH_URL = BASE_URL + '/search'
const ALBUM_URL = BASE_URL + '/albums/'
const TRACK_URL = BASE_URL + '/tracks/'
const ARTIST_URL = BASE_URL + '/artists/'
let token = ''

export async function get_token() {
  try {
    const response = await axios.post(
      TOKEN_URL,
      new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: process.env.SPOTIFY_CLIENT_ID,
        client_secret: process.env.SPOTIFY_CLIENT_SECRET
      })
    )
    token = response.data.access_token
    return true
  } catch (error) {
    console.error('not throwed error: ', error)
    return false
  }
}

async function get_token_if_not_exist() {
  if (token === '') {
    const results = await get_token()
    BrowserWindow.getFocusedWindow().webContents.send('get-token', results)
  }
}

export async function search(query) {
  await get_token_if_not_exist()
  try {
    const response = await axios.get(SEARCH_URL, {
      params: {
        q: query,
        type: 'album,artist,track'
      },
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    return response.data
  } catch (error) {
    console.error(error)
    return { error: true }
  }
}

export async function getAlbum(album_id) {
  await get_token_if_not_exist()
  try {
    const response = await axios.get(ALBUM_URL + album_id, {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    return response.data
  } catch (error) {
    console.error(error)
    return { error: true }
  }
}

export async function getTrack(track_id) {
  await get_token_if_not_exist()
  try {
    const response = await axios.get(TRACK_URL + track_id, {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    return response.data
  } catch (error) {
    console.error(error)
    return { error: true }
  }
}

export async function getArtistTopTrack(artist_id) {
  await get_token_if_not_exist()
  try {
    const response = await axios.get(ARTIST_URL + artist_id + '/top-tracks', {
      headers: {
        Authorization: 'Bearer ' + token
      }
    })
    return response.data
  } catch (error) {
    console.error(error)
    return { error: true }
  }
}
