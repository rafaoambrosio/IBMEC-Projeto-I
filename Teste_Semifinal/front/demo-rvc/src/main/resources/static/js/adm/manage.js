fetch('http://localhost:8080/adm')
    .then(response => response.json())
    .then(products => {
        const tbody = document.getElementById('product-table-body');
        products.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${product.id}</td>
                <td>${product.titulo}</td>
                <td>
                    <button onclick="deleteProduct(${product.id})">Delete</button>
                    <a href="/adm/edit/${product.id}">Edit</a>
                </td>
            `;
            tbody.appendChild(row);
        });
    })
    .catch(error => console.error('Error fetching products:', error));

function deleteProduct(id) {
    fetch('http://localhost:8080/adm/' + id, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            alert('Product deleted');
            location.reload();
        } else {
            alert('Error deleting product');
        }
    });
}