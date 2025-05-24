export interface QueryParams {
  type: string;
  inQuery?: boolean;
  inFunction?: boolean;
}

export const makeQuery = (
  name: string,
  params: Record<string, QueryParams>,
  fields: string[]
) => {
  const queryParams: string[] = [];
  const functionParams: string[] = [];

  for (const param in params) {
    const { type, inFunction = true, inQuery = true } = params[param];
    if (inQuery) queryParams.push("$" + `${param}: ${type}`);
    if (inFunction) functionParams.push(`${param}: ${param}`);
  }

  return `
    query (${queryParams.join(", ")}) {
        ${name}(${functionParams.join(", ")}) {
            ${fields.join("\n")}
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
