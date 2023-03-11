import axios from 'axios'
const apiKey = '0ca5fe98d6d244c3a5f5d753d0d5f5eb'

export const GetAutocompleteQuery = (text, cb) => {
    if (text === '') {
        cb()
    }
    console.log('https://api.geoapify.com/v1/geocode/autocomplete?text=' + text + '&apiKey=' + apiKey)
    const config = {
        method: 'get',
        url: 'https://api.geoapify.com/v1/geocode/autocomplete?text=' + text + '&apiKey=' + apiKey,
        headers: { }
    }
    axios(config)
        .then(response => {
            console.log(response)
            cb(response.data)
        })
        .catch(error => {
            console.log(error)
        })
}