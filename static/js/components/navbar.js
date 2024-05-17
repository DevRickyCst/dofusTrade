window.addEventListener('scroll', function() {
    var scrollPosition = this.window.scrollY;
    fadeOnScroll(scrollPosition, 50, 175, document.getElementById('title-navbar-expand'));
    retractSearchBar(scrollPosition);
  });

  function fadeOnScroll(scrollPosition, startFadePosition, stopFadePosition, element) {
    console.log("hello");
    var opacity = 1 - ((scrollPosition - startFadePosition) / (stopFadePosition - startFadePosition));
    if (opacity < 0) {
      opacity = 0;
    }
    element.style.opacity = opacity;
  }

  function retractSearchBar(scrollPosition) {
    var searchDiv = document.getElementById('search_div');
    var searchLabel = document.getElementById('search-label');
    if (scrollPosition >= 300) {
        searchDiv.style.width = '300px';
        searchLabel.style.opacity = 0;
    } else {
        searchDiv.style.width = '600px';
        searchLabel.style.opacity = 1;
    }
  }