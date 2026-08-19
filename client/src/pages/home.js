import { products } from "../mocks/mock-products.js";

export function renderHome() {
  const productsHtml = products
    .map(function (item) {
      return `
            <div class="product-card">
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <div class="product-price">${item.price} руб.</div>
                <button class="buy-btn">Купить</button>
            </div>
        `;
    })
    .join("");

  document.body.innerHTML = `
    <header class="main-header">
        <a href="/" class="logo">MySoft Shop</a>
        <nav class="nav-menu">
            <a href="/" class="nav-link active">Каталог</a>
        </nav>
        <a href="/cart" class="cart-link">Корзина</a>
    </header>

    <main class="container">
        <h1 class="page-title">Каталог товаров</h1>
        <div class="products-grid">${productsHtml}</div>
    </main>
  `;
}
