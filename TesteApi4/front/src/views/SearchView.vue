<template>
  <div class="search-view-container">
    <div class="input-search-container">
      <h1 class="main-title">Buscar operadora</h1>
      <input v-model="busca" type="text" placeholder="Digite o nome da operadora..." class="styled-input">

      <div v-if="resultados.length > 0">
        <h2 class="result-title">Resultados:</h2>
        <ul class="result-container">
          <li
            v-for="(item, index) in resultados"
            :key="index"
            class="results-list"
          >
            <p><strong>Razão Social:</strong> {{ item.Razao_Social }}</p>
            <p><strong>Nome Fantasia:</strong> {{ item.Nome_Fantasia }}</p>
            <p><strong>UF:</strong> {{ item.UF }}</p>
            <p><strong>Registro ANS:</strong> {{ item.Registro_ANS }}</p>
          </li>
        </ul>
      </div>

      <div v-else-if="busca.length >= 2 && !carregando" class="interval-container">
        <img src="https://www.chetanbharat.com/Backend/assets/images/no-data.png" alt="no-data"></img>
        <h3>Nenhum resultado encontrado.</h3>
      </div>

      <div v-if="carregando" class="interval-container">
        <img src="https://github.com/ingrydf12/intuitive-challenge/blob/master/TesteApi4/front/src/assets/outline-loading.gif?raw=true" alt="loading"></img>
        <h3>Estamos buscando...</h3>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import ApiService from "@/services/ApiService.js";

export default {
  setup() {
    const busca = ref("");
    const resultados = ref([]);
    const carregando = ref(false);

    const buscar = async () => {
  if (busca.value.length < 2) {
    resultados.value = [];
    return;
  }

  carregando.value = true;

  const response = await ApiService.search(busca.value);
  console.log("Dados recebidos:", response);
  resultados.value = response;

  carregando.value = false;
};


    watch(busca, buscar);

    return {
      busca,
      resultados,
      carregando,
      buscar,
    };
  },
};
</script>



<style scoped>

.search-view-container {
  width: 100%;
  margin: 0;
  justify-items: start;
}

.input-search-container {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: start;
}

.styled-input{
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.main-title {
  font-size: 2em;
  font-weight: bold;
  margin-bottom: 1rem;
  color: rgb(94, 224, 137);
}

.result-title{
  font-size: 1.2em;
  font-weight: 500;
  margin-bottom: 1rem;
  color: var(--color-text);
}

.results-list{
  margin-bottom: 1rem;
  border-radius: 0.5rem;
  width: 100%;
  list-style: none;
  height: fit-content;
  word-wrap: break-word;
  padding: 1rem;
  color: #fafafa;
  background-color: #113b31;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.result-container{
  position: absolute;
  display: block;
  max-width: 45%;
  max-height: 60%;
  flex-direction: column;
  padding: 0;
  overflow-y: auto;
}

.interval-container{
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    margin-top: 2rem;
    gap: 1rem;
    color: var(--color-text);
}

.interval-container img{
  width: 5rem;
  height: 5rem;
  object-fit: contain;
}

strong{
  font-weight: 700;
}

@media (max-width: 680px){
  .result-container{
    max-width: 90%;
    max-height: 100%;
  }

  .results-list{
    width: 100%;
  }
}

</style>