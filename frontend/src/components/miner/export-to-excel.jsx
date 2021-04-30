import React, {useEffect, useState} from "react";
import * as FileSaver from "file-saver";
import * as XLSX from "xlsx";
import Button from "react-bootstrap/Button";
import axios from "axios";

export const ExportToExcel = ({ fileId, api_host }) => {
    const fileType =
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
    const fileExtension = ".xlsx";
    const [exportData, setExportData] = useState(null)

    // The Effect Hook lets you perform side effects in function components
    // It combines componentDidMount, componentDidUpdate, and componentWillUnmount
    useEffect(() => {
        const request_url = `${api_host}/api/exportToCsv/${fileId}`
        const fetchData = () =>{
            // Axios GET request
            axios.get(request_url)
                // set returned csv data as state {exportData: data}
                .then((response) => {
                    setExportData(response)
                })
        }
        fetchData()
    }, [])

    // create Download with CSV file from exportData
    const exportToCSV = (apiData, fileId) => {
        const ws = XLSX.utils.json_to_sheet(apiData);
        const wb = { Sheets: { data: ws }, SheetNames: ["data"] };
        const excelBuffer = XLSX.write(wb, { bookType: "xlsx", type: "array" });
        const data = new Blob([excelBuffer], { type: fileType });
        // file is saved as e.g. "lawrgminer_export_3.xlsx"
        FileSaver.saveAs(data, "lawrgminer_export_" + fileId + fileExtension);
    };


    return (
        <Button className={"miner-results-export-btn"}
                variant="outline-light"
                onClick={() => exportToCSV(exportData, fileId)}>Export to CSV</Button>
    );
};