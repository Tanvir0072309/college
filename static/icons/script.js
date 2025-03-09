const ctx = document.getElementById('userChart').getContext('2d');

const userChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
      data: [2000, 2500, 3000, 2800, 3500, 4000, 4200],
      borderColor: '#f97316',
      borderWidth: 4,
      fill: false,
      backgroundColor: 'rgba(0, 123, 255, 0.2)',
      tension: 0.4,
    }]
  },
  options: {
    plugins: {
      legend: {
        display: false
      }
    },
    scales: {
      x: {
        grid: {
          display: true,
          color: '#d4c5d3'
        }
      },
      y: {
        grid: {
          drawBorder: true,
          color: '#d4c5d3'
        },
        ticks: {
          display: false
        }
      }
    },
    responsive: true,
    maintainAspectRatio: false,
  }
});

function toggleSwitch(element) {
  element.classList.toggle('active');
}
