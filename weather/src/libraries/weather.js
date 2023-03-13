import axios from 'axios'

export const GetWeatherQuery = ({ lat, lon }, cb) => {
    let encoded = ''
    if (lat !== undefined && lon !== undefined) {
        encoded = lat + '%2C' + lon + '?unitGroup=us' + '&contentType=json'
    } else{
        return cb(null, { error: 'No lat or lon provided' })
    }
    axios({
        method: 'post',
        url: 'http://localhost:8000/api/weather',
        data: {
            encoded: encoded
        },
        headers: { }
    })
        .then(response => {
            cb({ data: response.data })
        })
        .catch(error => {
            cb({ error: error })
        })
}
