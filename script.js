// static/script.js
function fetchAlerts() {
  fetch('/alerts')
    .then(res => res.json())
    .then(data => {
      const alertList = document.getElementById('alerts');
      alertList.innerHTML = '';
      data.forEach(alert => {
        const li = document.createElement('li');
        li.textContent = alert;
        alertList.appendChild(li);
      });
    });
}

setInterval(fetchAlerts, 2000); // update every 2 seconds
