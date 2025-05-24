<template>
  <div>
    <v-app>
      <v-app-bar app color="primary" dark>
        <v-toolbar-title>Publicaciones</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </v-app-bar>
      <v-main>
        <v-container>
          <!--  Filtros -->
          <v-form @submit.prevent="fetchPublicaciones">
            <v-row>
              <v-col cols="12" md="4">
                <v-text-field v-model="filtro.autor" label="Autor"></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field v-model="filtro.categoria" label="Categoria"></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-select v-model="filtro.publicada"
                  :items="[{ text: 'Publicada', value: true }, { text: 'No Publicada', value: false }]"
                  label="Estado"></v-select>
              </v-col>
            </v-row>
            <v-btn type="submit" color="primary">Filtrar</v-btn>
          </v-form>


          <!--  Lista de publicaciones -->
          <v-row>
            <v-col v-for="publicacion in publicaciones" :key="publicacion.id" cols="12" md=4>
              <v-card>
                <v-img :src="imagen_url" height="200px"></v-img>
                <v-card-title>{{ publicacion.titulo }}</v-card-title>
                <v-card-subtitle>{{ publicacion.autor }} - {{ publicacion.categoria }}</v-card-subtitle>
                <v-card-text>{{ publicacion.descripcion }}</v-card-text>
                <v-chip-group>
                  <v-chip v-for="etiqueta in publicacion.etiquetas" :key="etiqueta">{{ etiqueta }}</v-chip>
                </v-chip-group>
              </v-card>
            </v-col>
          </v-row>

        </v-container>
      </v-main>
    </v-app>
  </div>
</template>

<script setup>
import { makeQuery } from '../utils/query.utils';


const imagen_url =
  "https://www.svgrepo.com/show/508699/landscape-placeholder.svg";
const publicaciones = ref([]);
const filtro = ref({
  autor: "",
  categoria: "",
  publicada: null,
});

const fetchPublicaciones = async () => {
  const params = { filtro: { type: "PublicacionFilter" } };
  const fields = [
    "id",
    "titulo",
    "autor",
    "categoria",
    "descripcion",
    "publicada",
    "etiquetas",
  ];
  const query = makeQuery("publicaciones", params, fields);

  const variables = { filtro: filtro.value };
  const response = await fetch("http://localhost:8000/graphql", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query, variables }),
  });
  const result = await response.json();
  publicaciones.value = result.data.publicaciones;
};

watch(
  filtro,
  (newFiltro) => {
    fetchPublicaciones();
  },
  { deep: true }
);

// return { publicaciones, filtro, fetchPublicaciones };
</script>