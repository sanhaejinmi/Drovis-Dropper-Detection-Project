const cards = document.querySelectorAll(".main-section");

cards.forEach((card, index) => {
  card.style.cursor = "pointer";
  card.addEventListener("click", () => {
    console.log(`카드 ${index + 1} 클릭됨`);
    // window.location.href = `detail.html?id=${index + 1}`; // 이동도 가능
  });
});

