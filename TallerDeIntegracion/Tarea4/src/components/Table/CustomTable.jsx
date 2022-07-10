import * as React from "react";
import styles from "./customTable.module.css";
import { DataGrid } from "@mui/x-data-grid";
import { useState, useEffect } from "react";
import axios from "axios";
import { addDotsToNumber } from "../../utils";
import { style } from "@mui/system";

export default function CustomTable({ type }) {
  const [pageSize, setPageSize] = useState(25);
  const [page, setPage] = useState(0);
  const [sortBy, setSortBy] = useState(null);
  const [sortDirection, setSortDirection] = useState(null);
  const [loading, setLoading] = useState(false);
  const [rows, setRows] = useState([
    { id: 1, name: "Cargando...", price: "Cargando..." },
  ]);

  const getTitle = (type) => {
    switch (type) {
      case "trays":
        return "Bandejas";
      case "courses":
        return "Platos";
      case "ingredients":
        return "Ingredientes";
      default:
        return "Productos";
    }
  };

  const getData = async () => {
    try {
      const response = await axios.get(
        `/${type}?page=${page + 1}&size=${pageSize}${
          sortBy ? `&sort=${sortBy}&order=${sortDirection}` : ""
        }`
      );
      maskData(response.data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [pageSize, page, sortBy, sortDirection, type]);

  const maskData = (data) => {
    var arr = [];
    arr = Array.from(
      { length: page * pageSize },
      (_, i) => arr[i] ?? { id: i, name: "Cargando...", price: "Cargando..." }
    );
    arr.push(...data.items);
    arr.push(
      ...Array.from(
        { length: data.total - (page + 1) * pageSize },
        (_, i) =>
          arr[i] ?? { id: i + 1000, name: "Cargando...", price: "Cargando..." }
      )
    );
    setRows(
      arr.map((item) => ({
        id: item.id,
        name: item.name,
        price: `$${addDotsToNumber(item.price)}`,
      }))
    );
  };
  const columns = [
    { field: "id", hide: true },
    { field: "name", headerName: "Nombre", flex: 1, headerClassName: "header" },
    {
      field: "price",
      headerName: "Precio",
      flex: 1,
      headerClassName: "header",
    },
  ];

  const cellClickHandler = (cell) => {
    window.location.replace(`/producto/${cell.id}/${type}`);
  };

  const pageChangeHandler = (pageNumber) => {
    setPage(pageNumber);
  };

  const pageSizeHandler = (pageSize) => {
    setPageSize(pageSize);
  };

  const handleSortChange = (sorting) => {
    setSortBy(sorting.length === 0 ? null : sorting[0].field);
    setSortDirection(sorting.length === 0 ? null : sorting[0].sort);
  };

  return (
    <div>
      {type === "trays" ? <div className={styles.name}><h1>Bienvenido a Menú online de Restaurant TI!</h1> </div>: null}
      <div className={styles.title}>
        <h1>{getTitle(type)}</h1>
      </div>
      <div style={{ height: 400, width: "100%" }}>
        <DataGrid
          sx={{
            margin: "40px",
            "& .header": {
              backgroundColor: "rgba(255, 7, 0, 0.55)",
            },
          }}
          rows={rows}
          columns={columns}
          pageSize={pageSize}
          page={page}
          disableColumnFilter={true}
          disableColumnMenu={true}
          disableColumnSelector={true}
          disableDensitySelector={true}
          autoHeight={true}
          onCellClick={cellClickHandler}
          onPageChange={pageChangeHandler}
          onPageSizeChange={pageSizeHandler}
          sortingMode="server"
          onSortModelChange={handleSortChange}
          loading={loading}
        />
      </div>
    </div>
  );
}
