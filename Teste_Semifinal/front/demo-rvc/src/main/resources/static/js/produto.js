
            // Extract the product ID from the URL path
            const productId = window.location.pathname.split("/").pop();
    
            // Fetch product data from the API
            fetch(`http://localhost:8080/${productId}`)
                .then(response => response.json())
                .then(product => {
                    // Set product details
                    document.getElementById("tituloProduto").textContent = product.titulo;
                    document.getElementById("tipoProduto").textContent = product.tipo;
    
                    // Clear existing carousel indicators and items
                    const indicatorsContainer = document.getElementById("productImageCarouselIndicators");
                    const itemsContainer = document.getElementById("productImageCarouselItems");
                    indicatorsContainer.innerHTML = "";
                    itemsContainer.innerHTML = "";

                    let slideIndex = 0;

                    // Add videos to carousel
                    product.urlVideo.forEach((urlv, index) => {
                        // Create indicator
                        const indicator = document.createElement("li");
                        indicator.setAttribute("data-target", "#carouselExampleIndicators");
                        indicator.setAttribute("data-slide-to", slideIndex);
                        if (slideIndex === 0) indicator.classList.add("active");
                        indicatorsContainer.appendChild(indicator);

                        // Create carousel item
                        const carouselItem = document.createElement("div");
                        carouselItem.className = `carousel-item${slideIndex === 0 ? ' active' : ''}`;
                        
                        const iframe = document.createElement("iframe");
                        iframe.src = urlv.replace("watch?v=", "embed/");
                        iframe.className = "d-block w-100";
                        iframe.frameborder = "0";
                        iframe.allowfullscreen = true;
                        iframe.alt = `Slide ${slideIndex + 1}`;
                        
                        carouselItem.appendChild(iframe);
                        itemsContainer.appendChild(carouselItem);
                        
                        slideIndex++;
                    });

                    // Add images to carousel
                    product.imagens.forEach(imagem => {
                        // Create indicator
                        const indicator = document.createElement("li");
                        indicator.setAttribute("data-target", "#carouselExampleIndicators");
                        indicator.setAttribute("data-slide-to", slideIndex);
                        if (slideIndex === 0) indicator.classList.add("active");
                        indicatorsContainer.appendChild(indicator);

                        // Create carousel item
                        const carouselItem = document.createElement("div");
                        carouselItem.className = `carousel-item${slideIndex === 0 ? ' active' : ''}`;
                        
                        const img = document.createElement("img");
                        img.src = `data:image/jpeg;base64,${imagem.bytes}`;
                        img.className = "d-block w-100";
                        img.alt = `Slide ${slideIndex + 1}`;
                        
                        carouselItem.appendChild(img);
                        itemsContainer.appendChild(carouselItem);
                        
                        slideIndex++;
                    });

                    document.getElementById("productAccordeonLocalizacao").textContent = product.localizacao;
                    document.getElementById("productAccordeonDescricao").textContent = product.descricao;

                    const ulInclusos = document.getElementById("productAccordeonInclusos")
                    product.itensInclusos.forEach(item => {
                        const li = document.createElement("li");
                        const p = document.createElement("p");
                        const strong = document.createElement("strong");
                        strong.textContent = item;
                        p.appendChild(strong);
                        li.appendChild(p);
                        ulInclusos.appendChild(li);
                    });
                    
                    const ulDicas = document.getElementById("productAccordeonDicas")
                    product.dicas.forEach(dica => {
                        const li = document.createElement("li");
                        const p = document.createElement("p");
                        const strong = document.createElement("strong");
                        strong.textContent = dica;
                        p.appendChild(strong);
                        li.appendChild(p);
                        ulDicas.appendChild(li);
                    });

                    const ulObservacoes = document.getElementById("productAccordeonObservacoes")
                    product.observacoes.forEach(obs => {
                        const li = document.createElement("li");
                        const p = document.createElement("p");
                        const strong = document.createElement("strong");
                        strong.textContent = obs;
                        p.appendChild(strong);
                        li.appendChild(p);
                        ulObservacoes.appendChild(li);
                    });

                    document.getElementById("productAccordeonRoteiro").textContent = product.roteiro;

                    document.getElementById("productNumeroDiarias").textContent = product.numeroDiarias;
                    document.getElementById("productHospedagem").textContent = product.hospedagemInclusa ? "Sim" : "Não";
                    document.getElementById("productLimiteVagas").textContent = product.limiteVagas;

                    const ulDatas = document.getElementById("productDatasDisponiveis")
                    product.dataDisponiveis.forEach(dateString => {
                        const li = document.createElement("li");
                        const date = new Date(dateString);
                        li.textContent = date.toLocaleDateString("en-GB"); // Format as dd/MM/yyyy
                        ulDatas.appendChild(li);
                    });

                    const precoHeads = document.getElementById("productFaixaPrecoHeads");
                    const precoCols = document.getElementById("productFaixaPrecoCols");

                    product.faixaPreco.forEach(range => {
                        const th = document.createElement("th");
                        th.innerHTML = `<p>${range.faixa}</p>`;
                        precoHeads.appendChild(th);
                        const td = document.createElement("td");
                        td.innerHTML = `<p>R$ ${range.preco}</p>`;
                        precoCols.appendChild(td);
                    });
                })
                .catch(error => console.error("Error fetching product data:", error));
        

        
        document.addEventListener("DOMContentLoaded", function () {
            const buttons = document.querySelectorAll(".btn-link");

            buttons.forEach((button) => {
                button.addEventListener("click", function () {
                    const target = document.querySelector(this.getAttribute("data-target"));
                    const isCollapsed = target.classList.contains("show");

                    if (isCollapsed) {
                        this.classList.remove("active");
                    } else {
                        this.classList.add("active");
                    }
                });
            });
        });
    