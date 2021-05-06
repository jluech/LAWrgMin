import React from "react";
import Button from "react-bootstrap/Button";
import axios from "axios";
import FileSaver from "file-saver";
import XLSX from "xlsx";

export const ExportToExcel = (props) => {
    const fileType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
    const fileExtension = ".xlsx";

    // create download with CSV file from exportData
    const exportToCSV = () => {
        const request_url = `${props.api_host}/api/exportToCsv/${props.fileId}`
        axios.get(request_url)
            .then((response) => {
                const ws = XLSX.utils.aoa_to_sheet(response.data);
                const wb = {Sheets: {data: ws}, SheetNames: ["data"]};
                const excelBuffer = XLSX.write(wb, {bookType: "xlsx", type: "array"});
                const data = new Blob([excelBuffer], {type: fileType});

                // file is saved as e.g. "lawrgminer_export.xlsx"
                FileSaver.saveAs(data, "lawrgminer_export" + fileExtension);
            })
            .catch((err) => {
                console.log("error during request:", request_url, "\n", err);
                alert(`Something went wrong!\nError during request: ${request_url}`);
            });
    };

    return (
        <Button className={"miner-results-export-btn"}
                variant="outline-light"
                onClick={exportToCSV}
        >Export to CSV</Button>
    );
};
