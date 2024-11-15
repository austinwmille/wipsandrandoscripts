// Sample data for main categories and anime characters
const categories = [
    { name: "Crunchyroll", image: "images/category1.png" },
    { name: "Box Lunch", image: "images/category2.png" },
    { name: "Amazon", image: "images/category3.png" }
];

const characters = [
    { name: "Character 1", image: "images/character1.png" },
    { name: "Character 2", image: "images/character2.png" },
    { name: "Character 3", image: "images/character3.png" },
    { name: "Character 4", image: "images/character4.png" },
    { name: "Character 5", image: "images/character5.png" },
    { name: "Character 6", image: "images/character6.png" },
    { name: "Character 7", image: "images/character7.png" },
    { name: "Character 8", image: "images/character8.png" },
    { name: "Character 9", image: "images/character9.png" },
    { name: "Character 10", image: "images/character10.png" },
    { name: "Character 11", image: "images/character11.png" },
    { name: "Character 12", image: "images/character12.png" }
];

// Function to populate categories
function populateCategories() {
    const categoryGrid = document.querySelector('.category-grid');
    categories.forEach(cat => {
        const catDiv = document.createElement('div');
        catDiv.classList.add('category-item');
        catDiv.innerHTML = `<img src="${cat.image}" alt="${cat.name}"><p>${cat.name}</p>`;
        categoryGrid.appendChild(catDiv);
    });
}

// Function to populate anime characters
function populateCharacters() {
    const characterGrid = document.querySelector('.character-grid');
    characters.forEach(char => {
        const charDiv = document.createElement('div');
        charDiv.classList.add('character-item');
        charDiv.innerHTML = `<img src="${char.image}" alt="${char.name}"><p>${char.name}</p>`;
        characterGrid.appendChild(charDiv);
    });
}

// Initialize the content on page load
document.addEventListener('DOMContentLoaded', () => {
    populateCategories();
    populateCharacters();
});
