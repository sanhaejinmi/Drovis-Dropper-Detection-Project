// 📁 파일: history.js

// 📌 카드 클릭 이벤트 설정
const cards = document.querySelectorAll(".main-section");

cards.forEach((card, index) => {
  card.style.cursor = "pointer";
  card.addEventListener("click", () => {
    console.log(`카드 ${index + 1} 클릭됨`);
    // 예: 상세 페이지 이동 가능
    // window.location.href = `detail.html?id=${index + 1}`;
  });
});

// 📌 "New" 버튼 클릭 시 predict.html로 이동
const newButton = document.getElementById("new-button");

if (newButton) {
  newButton.style.cursor = "pointer"; // 마우스 올리면 포인터 표시
  newButton.addEventListener("click", () => {
    console.log("✅ 이동 시도 중: /web/predict/predict.html");
    window.location.href = "/web/predict/predict.html";
  });
} else {
  console.error("❌ new-button 요소를 찾을 수 없습니다.");
}
