function apiloader(){
    return fetch('http://127.0.0.1:5000')
    .then(response => response.json())
    .then(data => {
        // Manipule os dados recebidos da API
        return data;
})
    .catch(error => {
        // Trate erros
        console.error(error);
    });}