document.addEventListener('DOMContentLoaded', function() {
    // Получаем ссылки на элементы
    const container = document.querySelector('.container');
    const image = document.querySelector('.image');
    const previousButton = document.querySelector('.button.previous');
    const nextButton = document.querySelector('.button.next');
  
    // Массив с путями к изображениям
    const images = [
      'город.jpg',
      'природа.jpg',
      'изображение2.jpg',
    ];
  
    let currentIndex = images.length - 1; // Текущий индекс изображения
  
    // Функция для обновления отображаемого изображения
    function updateImage() {
      image.src = images[currentIndex];
  
      // Проверка на достижение последнего изображения
      if (currentIndex === images.length - 1) {
        currentIndex = 0;
      }
      // Проверка на достижение первого изображения
      else if (currentIndex === 0) {
        currentIndex = images.length - 1;
      }
    }
  
    // Обработчик события для кнопки "Назад"
    previousButton.addEventListener('click', function() {
      currentIndex--;
      if (currentIndex < 0) {
        currentIndex = images.length - 1;
      }
      updateImage();
    });
  
    // Обработчик события для кнопки "Вперед"
    nextButton.addEventListener('click', function() {
      currentIndex++;
      if (currentIndex >= images.length) {
        currentIndex = 0;
      }
      updateImage();
    });
  
    // Инициализация отображаемого изображения
    updateImage();
  });
  function updateImage() {
    image.src = images[currentIndex];
    
    // Обновление текущего номера изображения
    const currentImageNumberElement = document.querySelector('.current-image-number');
    currentImageNumberElement.textContent = currentIndex + 1;
    
    // Обновление общего количества изображений
    const totalImageNumberElement = document.querySelector('.total-image-number');
    totalImageNumberElement.textContent = images.length;
    
    // Проверка на достижение последнего изображения
    if (currentIndex === images.length - 1) {
      currentIndex = 0;
    }
    // Проверка на достижение первого изображения
    else if (currentIndex === 0) {
      currentIndex = images.length - 1;
    }
  }
  