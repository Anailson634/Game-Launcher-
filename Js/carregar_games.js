const childe = document.querySelector(".container");
apiloader()
.then (data => {
    for (const chave in data) {
        let newDiv=document.createElement("div");
        let img=data[chave]['Ico'];

        newDiv.classList.add(`capa`);
        newDiv.classList.add(chave)
        childe.appendChild(newDiv);
        

        let objimg=document.querySelector(`.${chave}`)
        objimg.style.backgroundImage=`url("Imagens/${img}")`
    }
})
//${data[chave]["Ico"]}