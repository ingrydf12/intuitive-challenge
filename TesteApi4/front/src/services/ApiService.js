import axios from "axios";

const ApiService = {
  async search(input) {
    try {
      const response = await axios.get(
        `https://intituivechallenge.onrender.com/api/search?q=${input}`
      );
      return response.data;
    } catch (error) {
      console.error("Erro na busca:", error);
      return [];
    }
  },
};

export default ApiService;