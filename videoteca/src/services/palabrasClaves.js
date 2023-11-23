import axiosInstance from "../axios";

const API_URL = "http://localhost:8000/palabrasclaves/";

/**
 * Función para consultar todas las palabras claves registradas en la base de datos.
 * @returns Data enviada desde el backend
 */
export const ListPalabrasClaves = async () => {
  const response = await axiosInstance.get(API_URL);
  if (response.status === 200) {
    return await response.data;
  }
};

export const RegisterPalabrasClaves = async (newPalabrasClaves) => {
  const response = await axiosInstance.post(API_URL, newPalabrasClaves);
  if (response.status === 200) {
    return await response.data;
  }
};

export const getPalabrasClaves = async (palabrasClavesID) => {
  const response = await axiosInstance.get(`${API_URL}${palabrasClavesID}`);
  if (response.status === 200) {
    return await response.data;
  }
};

export const updatePalabrasClaves = async(id,updpalabrasClaves) =>{
  const response = await axiosInstance.patch(API_URL+id+"/",updpalabrasClaves);
  if (response.status === 200) {
      return response.data;
  }
}