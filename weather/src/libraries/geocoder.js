import axios from 'axios'

export const GetAutocompleteQuery = (text, cb) => {
    if (text === '') {
        cb()
    }
    const config = {
        method: 'post',
        url: 'http://localhost:8000/api/autocomplete',
        data: {
            query: text
        },
        headers: {}
    }
    axios(config)
        .then(response => {
            cb(response.data)
        })
        .catch(error => {
            console.log(error)
        })
}

export const reverseGeocode = ({lat, lon}, cb) => {
    var config = {
        method: 'post',
        url: `http://localhost:8000/api/reverse-geocode`,
        data: {
            lat: lat,
            lon: lon
        },
        headers: { }
      };
      
      axios(config)
      .then(function (response) {
        cb(response.data.features[0])
      })
      .catch(function (error) {
        console.log(error);
      });
}