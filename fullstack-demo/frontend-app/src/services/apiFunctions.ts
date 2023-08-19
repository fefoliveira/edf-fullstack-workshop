import axios from "axios";
import { itemType } from "../types/itemType";

export function criarItem(item: itemType) {
    return axios.post("http://localhost:5000/items/", item);
}

export function todosItems() {
    return axios.get("http://localhost:5000/items/");
}

export function deleteItem(id: number) {
    return axios.delete(`http://localhost:5000/items/${id}`);
}