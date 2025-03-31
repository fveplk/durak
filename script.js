const socket = new WebSocket("ws://localhost:8000/ws/test_session");

// Отправка хода на сервер
function playCard(card) {
    socket.send(JSON.stringify({
        type: "play_card",
        card: card
    }));
}

// Отрисовка карт
function renderCards(cards) {
    const container = document.getElementById("player-cards");
    container.innerHTML = cards.map(card => 
        `<div class="card" onclick="playCard('${card}')">${card}</div>`
    ).join("");
}

// Обновление игры через WebSocket
socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.type === "game_update") {
        console.log(data.message);
    }
};

// Пример начальной раздачи карт
renderCards(["6♥", "7♦", "8♣", "9♠", "10♥", "J♦"]);