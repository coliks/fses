document.addEventListener('DOMContentLoaded', () => {
    const profileMenuButton = document.getElementById('profile-menu-button');
    const profileMenu = document.getElementById('profile-menu');

    profileMenuButton.addEventListener('click', () => {
        if (profileMenu.classList.contains('max-h-0')) {
            profileMenu.classList.remove('max-h-0', 'opacity-0');
            profileMenu.classList.add('max-h-96', 'opacity-100');
        } else {
            profileMenu.classList.add('max-h-0', 'opacity-0');
            profileMenu.classList.remove('max-h-96', 'opacity-100');
        }
    })
})