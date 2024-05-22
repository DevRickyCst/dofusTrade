
window.addEventListener("load", function() {
    if (!document.getElementById('title-navbar-expand')) {
        var searchInput = document.getElementsByClassName('navbar-search-retracted');
        searchInput[0].style.opacity = 1;
    }
});

window.addEventListener('scroll', function() {
    var scrollPosition = this.window.scrollY;
    if (document.getElementById('title-navbar-expand')) {
        fadeOnScroll(scrollPosition, 50, 175, document.getElementById('title-navbar-expand'));
        retractSearchBar(scrollPosition);
    }
});

function fadeOnScroll(scrollPosition, startFadePosition, stopFadePosition, element) {
    var opacity = 1 - ((scrollPosition - startFadePosition) / (stopFadePosition - startFadePosition));
    if (opacity < 0) {
      opacity = 0;
    }
    element.style.opacity = opacity;
}

function retractSearchBar(scrollPosition) {
    var searchDiv = document.getElementById('search_div');
    var searchInput = document.getElementsByClassName('navbar-search-retracted');
    var searchLabel = document.getElementById('search-label');
    if (scrollPosition >= 350) {
        searchDiv.style.width = '900px';
        //searchDiv.style.left = '70%';
        searchDiv.style.opacity = 0;
        searchInput[0].style.opacity = 1;
        searchLabel.style.opacity = 0;
    } else {
        searchDiv.style.width = '600px';
        //searchDiv.style.left = '50%';
        searchLabel.style.opacity = 1;
        searchInput[0].style.opacity = 0;
        searchDiv.style.opacity = 1;
    }
}