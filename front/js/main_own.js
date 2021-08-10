'use strict'
if (document.querySelector('.slider')) {
    const swiper = new Swiper('.swiper-container', {
        // Optional parameters
        loop: true,
        navigation: {
            nextEl: '.swiper-next',
            prevEl: '.swiper-prev',
            autoplay: {
                delay: 2500,
            }
        }
    });
}

const links = document.querySelectorAll('.item-list__link[data-goto]')

if (links.length > 0) {
    links.forEach(link => {
        link.addEventListener('click', onMenuLinkClick);
    });
}

function onMenuLinkClick(e) {
    const link = e.target;
    if (link.dataset.goto && document.querySelector(link.dataset.goto)) {
        e.preventDefault();
        const gotoBlock = document.querySelector(link.dataset.goto);
        const gotoBlockValue = gotoBlock.getBoundingClientRect().top + window.pageYOffset - document.querySelector('header').offsetHeight;
        window.scrollTo({
            top: gotoBlockValue,
            behavior: "smooth"
        })

    }

};