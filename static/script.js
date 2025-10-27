async function getWeather() {
  console.log("JS Running....!");
  const city = document.getElementById("city").value;
  const resultDiv = document.getElementById("result");

  if (!city) {
    resultDiv.innerText = "⚠️ Please enter a city name!";
    return;
  }

  resultDiv.innerHTML = "⏳ Fetching weather data...";

  try {
    const response = await fetch("/getWeather", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ city }),
    });

    const data = await response.json();

    if (data.error) {
      resultDiv.innerText = "❌ Error: " + data.error;
    } else {
      resultDiv.innerHTML = `
            📍 City: ${data.city}<br>
            🌡 Temperature: ${data.temperature}°C<br>
            💧 Humidity: ${data.humidity}%<br>
            ☁️ Condition: ${data.condition}
            `;
    }
  } catch (error) {
    resultDiv.innerText = "❌ Error fetching data! ";
  }
}
