import { writable, get } from "svelte/store";

export const mode = writable("light");

// Retrieve user data from localStorage if available
const storedUserData = localStorage.getItem('userData');
const initialUserData = storedUserData ? JSON.parse(storedUserData) : {
  userId: 1714884,
  name: "Andy Tran",
  email: "aqtran@ualberta.ca",
  github: ""
};
export const currentUser = writable(initialUserData);

// Function to get the current value of currentUser
export function getCurrentUser() {
  return get(currentUser);
}

export const authToken = writable(localStorage.getItem("authToken") || "");

authToken.subscribe((val) => localStorage.setItem("authToken", val));
// Subscribe to changes in currentUser and update localStorage
currentUser.subscribe(value => {
  localStorage.setItem('userData', JSON.stringify(value));
});

export const hasNotifications = writable(false);
export const isLoginPage = writable(false);
