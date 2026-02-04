document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('city-input');
    const searchBtn = document.getElementById('search-btn');
    const weatherCard = document.getElementById('weather-card');
    const loader = document.getElementById('loader');
    const errorMessage = document.getElementById('error-message');

    // UI Elements
    const cityNameEl = document.getElementById('city-name');
    const countryNameEl = document.getElementById('country-name');
    const tempEl = document.getElementById('temperature');
    const tempUnitEl = document.getElementById('temp-unit');
    const humidityEl = document.getElementById('humidity');
    const windEl = document.getElementById('wind');

    searchBtn.addEventListener('click', fetchWeather);
    cityInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') fetchWeather();
    });

    async function fetchWeather() {
        const city = cityInput.value.trim();
        if (!city) return;

        // Reset UI
        weatherCard.classList.add('hidden');
        errorMessage.classList.add('hidden');
        loader.classList.remove('hidden');

        try {
            const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Weather data not found');
            }

            updateUI(data);
        } catch (error) {
            showError(error.message);
        } finally {
            loader.classList.add('hidden');
        }
    }

    function updateUI(data) {
        cityNameEl.textContent = data.city;
        countryNameEl.textContent = data.country || 'N/A';
        tempEl.textContent = Math.round(data.temp);
        tempUnitEl.textContent = data.units.temp;
        humidityEl.textContent = `${data.humidity}%`;
        windEl.textContent = `${data.wind_speed} ${data.units.speed}`;

        weatherCard.classList.remove('hidden');
    }

    function showError(message) {
        weatherCard.classList.add('hidden');
        errorMessage.classList.remove('hidden');
    }
});
