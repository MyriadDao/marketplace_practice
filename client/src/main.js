import { renderHome } from "./pages/home.js";

const path = window.location.pathname;

if (path === "/") {
  renderHome();
} else if (path === "/cart") {
  document.body.innerHTML = "<h1>Корзина</h1>";
} else {
  document.body.innerHTML = "<h1>Страница не найдена</h1>";
}
