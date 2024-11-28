document.getElementById('edit-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    // Collecting form values
    const form = event.target;
    
    const titulo = form.titulo.value;
    const descricao = form.descricao.value;
    const localizacao = form.localizacao.value;
    const resumo = form.resumo.value;
    const urlVideo = Array.from(form.querySelectorAll("input[name='urlVideo[]']")).map(input => input.value);
    const numeroDiarias = parseInt(form.numeroDiarias.value, 10);
    const hospedagemInclusa = form.hospedagemInclusa.value === "true";
    const roteiro = form.roteiro.value;
    const limiteVagas = parseInt(form.limiteVagas.value, 10);

    // Collecting dynamic lists
    const itensInclusos = Array.from(form.querySelectorAll("input[name='itemIncluso[]']")).map(input => input.value);
    const dicas = Array.from(form.querySelectorAll("input[name='dica[]']")).map(input => input.value);
    const observacoes = Array.from(form.querySelectorAll("input[name='observacao[]']")).map(input => input.value);
    const datasDisponiveis = Array.from(form.querySelectorAll("input[name='datasDisponiveis[]']")).map(input => input.value);

    // Collecting dynamic table data for FaixaPreco
    const faixaPreco = [];
    const faixaInputs = form.querySelectorAll("input[name='faixa[]']");
    const precoAlta1Inputs = form.querySelectorAll("input[name='precoAlta1[]']");
    const precoAlta2Inputs = form.querySelectorAll("input[name='precoAlta2[]']");
    const precoAlta3Inputs = form.querySelectorAll("input[name='precoAlta3[]']");
    const precoBaixa1Inputs = form.querySelectorAll("input[name='precoBaixa1[]']");
    const precoBaixa2Inputs = form.querySelectorAll("input[name='precoBaixa2[]']");
    const precoBaixa3Inputs = form.querySelectorAll("input[name='precoBaixa3[]']");
    for (let i = 0; i < faixaInputs.length; i++) {
        faixaPreco.push([faixaInputs[i].value, precoAlta1Inputs[i].value, precoAlta2Inputs[i].value, precoAlta3Inputs[i].value, precoBaixa1Inputs[i].value, precoBaixa2Inputs[i].value, precoBaixa3Inputs[i].value]);
    }

    const tipo = form.tipo.value;
    const imagens = await convertImagesToBase64();
    

    // Creating the JSON object
    const data = {
        titulo,
        descricao,
        localizacao,
        resumo,
        itensInclusos,
        dicas,
        observacoes,
        faixaPreco,
        urlVideo,
        numeroDiarias,
        hospedagemInclusa,
        roteiro,
        dataDisponiveis: datasDisponiveis,
        limiteVagas,
        tipo,
        imagens
    };

    // Posting the JSON data to the specified endpoint
    const productId = window.location.pathname.split('/').pop();
    fetch(("http://localhost:8080/adm/" + productId), {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log("Success:", result);
        alert("Form submitted successfully!");
    })
    .catch(error => {
        console.error("Error:", error);
        alert("There was an error submitting the form.");
    });
});

function addInput(containerId, name) {
    const container = document.getElementById(containerId);
    const inputGroup = document.createElement('div');
    const input = document.createElement('input');
    input.type = 'text';
    input.name = name + '[]';
    input.required = true;
    const removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.innerText = 'Remove';
    removeBtn.onclick = () => container.removeChild(inputGroup);
    inputGroup.appendChild(input);
    inputGroup.appendChild(removeBtn);
    container.appendChild(inputGroup);
}

function addRow() {
    const table = document.getElementById('faixasPreco');
    const row = document.createElement('tr');
    const row2 = document.createElement('tr');

    const faixaCell = document.createElement('td');
    const faixaInput = document.createElement('input');
    faixaInput.type = 'text';
    faixaInput.name = 'faixa[]';
    faixaInput.required = true;
    faixaCell.appendChild(faixaInput);

    const precoCellAlta1 = document.createElement('td');
    const precoInput1 = document.createElement('input');
    precoInput1.type = 'text';
    precoInput1.name = 'precoAlta1[]';
    precoInput1.required = true;
    precoCellAlta1.appendChild(precoInput1);

    const precoCellAlta2 = document.createElement('td');
    const precoInput2 = document.createElement('input');
    precoInput2.type = 'text';
    precoInput2.name = 'precoAlta2[]';
    precoInput2.required = true;
    precoCellAlta2.appendChild(precoInput2);

    const precoCellAlta3 = document.createElement('td');
    const precoInput3 = document.createElement('input');
    precoInput3.type = 'text';
    precoInput3.name = 'precoAlta3[]';
    precoInput3.required = true;
    precoCellAlta3.appendChild(precoInput3);

    const precoCellBaixa1 = document.createElement('td');
    const precoInput4 = document.createElement('input');
    precoInput4.type = 'text';
    precoInput4.name = 'precoBaixa1[]';
    precoInput4.required = true;
    precoCellBaixa1.appendChild(precoInput4);

    const precoCellBaixa2 = document.createElement('td');
    const precoInput5 = document.createElement('input');
    precoInput5.type = 'text';
    precoInput5.name = 'precoBaixa2[]';
    precoInput5.required = true;
    precoCellBaixa2.appendChild(precoInput5);

    const precoCellBaixa3 = document.createElement('td');
    const precoInput6 = document.createElement('input');
    precoInput6.type = 'text';
    precoInput6.name = 'precoBaixa3[]';
    precoInput6.required = true;
    precoCellBaixa3.appendChild(precoInput6);

    const removeCell = document.createElement('td');
    const removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.innerText = 'Remove';
    removeBtn.onclick = () => table.removeChild(row) && table.removeChild(row2);
    removeCell.appendChild(removeBtn);

    const emptyCell = document.createElement('td');
    const emptyCell2 = document.createElement('td');

    row.appendChild(faixaCell);
    row.appendChild(precoCellAlta1);
    row.appendChild(precoCellAlta2);
    row.appendChild(precoCellAlta3);
    row.appendChild(emptyCell);

    row2.appendChild(emptyCell2);
    row2.appendChild(precoCellBaixa1);
    row2.appendChild(precoCellBaixa2);
    row2.appendChild(precoCellBaixa3);
    row2.appendChild(removeCell);

    table.appendChild(row);
    table.appendChild(row2);
}

function addDate() {
    const container = document.getElementById('datasDisponiveis');
    const inputGroup = document.createElement('div');
    const input = document.createElement('input');
    input.type = 'date';
    input.name = 'datasDisponiveis[]';
    input.required = true;
    const removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.innerText = 'Remove';
    removeBtn.onclick = () => container.removeChild(inputGroup);
    inputGroup.appendChild(input);
    inputGroup.appendChild(removeBtn);
    container.appendChild(inputGroup);
}

function addImageRow() {
    const container = document.getElementById('imagens');
    const inputGroup = document.createElement('div');
    const input = document.createElement('input');
    input.type = 'file';
    input.name = 'imagens[]';
    input.accept = 'image/*';
    input.required = true;
    const removeBtn = document.createElement('button');
    removeBtn.type = 'button';
    removeBtn.innerText = 'Remove';
    removeBtn.onclick = () => container.removeChild(inputGroup);
    inputGroup.appendChild(input);
    inputGroup.appendChild(removeBtn);
    container.appendChild(inputGroup);
}

async function convertImagesToBase64() {
    const imageInputs = document.getElementsByName('imagens[]');
    const promises = [];
    
    for (const input of imageInputs) {
        if (input.files && input.files[0]) {
            const file = input.files[0];
            promises.push(new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onloadend = () => {
                    const base64String = reader.result.split(',')[1]; // Remove o prefixo data:*/*;base64,
                    resolve(base64String);
                };
                reader.onerror = reject;
                reader.readAsDataURL(file);
            }));
        }
    }
    
    return Promise.all(promises);
}