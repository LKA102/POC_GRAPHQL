// query.utils.ts
var makeQuery = (name, params, fields) => {
  const queryParams = [];
  const functionParams = [];
  for (const param in params) {
    const { type, inFunction = true, inQuery = true } = params[param];
    if (inQuery) queryParams.push("$" + `${param}: ${type}`);
    if (inFunction) functionParams.push(`${param}: ${param}`);
  }
  return `
    query (${queryParams.join(", ")}) {
        ${name}(${functionParams.join(", ")}) {
            ${fields.join(`\n`)}
        }
    }
  `;
};
makeQuery("publicaciones", { filtro: { type: "PublicacionFilter" } }, [
  "id",
  "titulo",
  "autor",
  "categoria",
  "descripcion",
  "publicada",
  "etiquetas",
]);
export { makeQuery };
