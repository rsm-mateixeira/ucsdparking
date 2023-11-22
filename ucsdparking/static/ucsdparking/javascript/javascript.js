document.addEventListener("DOMContentLoaded", function () {
    // Dropdown functionality
    var dropdown = document.querySelector('.dropdown');
    if (dropdown) {
        dropdown.addEventListener('click', function(event) {
            event.stopPropagation();
            this.querySelector('.dropdown-content').classList.toggle('show');
        });
    }

    window.onclick = function(event) {
        if (!event.target.matches('.dropdown, .dropdown *')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                if (dropdowns[i].classList.contains('show')) {
                    dropdowns[i].classList.remove('show');
                }
            }
        }
    };

    // Slideshow functionality
    var slides = document.getElementsByClassName("slide");
    var currentSlideIndex = 0;
    var interval;

    function showSlide(index) {
        var newTransformValue = "translateX(-" + index * 100 + "%)";
        document.getElementById("heroImage").style.transform = newTransformValue;
    }

    function nextSlide() {
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        showSlide(currentSlideIndex);
    }

    function prevSlide() {
        currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        showSlide(currentSlideIndex);
    }

    var nextBtn = document.getElementById("nextBtn");
    var prevBtn = document.getElementById("prevBtn");

    if (nextBtn) {
        nextBtn.addEventListener("click", function () {
            nextSlide();
            resetInterval();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener("click", function () {
            prevSlide();
            resetInterval();
        });
    }

    function startInterval() {
        interval = setInterval(nextSlide, 5000);
    }

    function resetInterval() {
        clearInterval(interval);
        startInterval();
    }

    startInterval();
});
