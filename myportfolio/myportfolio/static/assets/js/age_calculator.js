function age(birthdate) {
  const today = new Date();
  const age = today.getFullYear() - birthdate.getFullYear() - 
             (today.getMonth() < birthdate.getMonth() || 
             (today.getMonth() === birthdate.getMonth() && today.getDate() < birthdate.getDate()));
  return age;
}

const birthdate = new Date(1993, 10, 10); 
const ageValue = age(birthdate);

// Update the age in the HTML
const ageElement = document.getElementById("my_age");
ageElement.querySelector("span").textContent = ageValue;