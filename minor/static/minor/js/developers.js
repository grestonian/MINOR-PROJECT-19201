const devCards= ()=> {
    const devBtn = document.querySelector('.devCardsClick');
    const backContainer = document.querySelector('.container');
    const devContainer = document.querySelector('.developers-container')
    devBtn.addEventListener('click', () => {
        devContainer.classList.toggle('developers-container-toggle')
        backContainer.classList.toggle('container-tog')

    });
}

devCards();