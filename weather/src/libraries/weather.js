import axios from 'axios'

const apiKey = 'GBDQESSQSEFC9JNRKB5Q8RXB8'

export const GetWeatherQuery = ({ lat, lon }, cb) => {
    let encoded = ''
    if (lat !== undefined && lon !== undefined) {
        encoded = lat + '%2C' + lon + '?unitGroup=us&key=' + apiKey + '&contentType=json'
    } else{
        return cb(null, { error: 'No lat or lon provided' })
    }
    console.log('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + encoded)
    axios({
        method: 'get',
        url: 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + encoded,
        headers: { }
    })
        .then(response => {
            cb({ data: response.data })
        })
        .catch(error => {
            cb({ error: error })
        })
}
