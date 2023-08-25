apiloader()
.then(date => {
    for (const chave in date){
        let DivGame=document.querySelector(`.${chave}`)
        
        DivGame.addEventListener("click", async () => {
          const init={
            method: 'POST', // Método da requisição (POST para enviar dados)
            headers: {
              'Content-Type': 'application/json', // Tipo de conteúdo é JSON
            },
            body: JSON.stringify({'Game': `${date[chave]['Exe']}`}), // Converte o objeto para JSON
          }
          const response = await fetch('http://127.0.0.1:5000/iniciar', init)
          const dados = await response.json()
        })
    }
})