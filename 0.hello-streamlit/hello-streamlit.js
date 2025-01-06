function handleSubmit() {
  const userInput = document.getElementById("userInput").value;
  const output = document.getElementById("output");
  if (userInput.trim()) {
    output.textContent = `你輸入了：${userInput}`;
  } else {
    output.textContent = "請輸入有效內容！";
  }
}
