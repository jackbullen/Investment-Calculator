const TICKERS = ["NASDAQ:AAPL", "NASDAQ:GOOG", "NASDAQ:MSFT", "NASDAQ:TSLA", "NYSE:GM", "NYSE:F", "TSE:TD", "TSE:BNS", "TSE:RY"]
const ID = "MY_SHEET_ID";
const Sheet = SpreadsheetApp.openById(ID).getSheetByName("stock_data")

function getCellAddress(row, col) {
  var columnLetter = String.fromCharCode(65+col); // Convert column number to letter
  var cellAddress = columnLetter + row.toString();
  return cellAddress;
}

function loadStockData(){
  for (var col = 0; col <= TICKERS.length; col++){

    // Set the ticker name above the GOOGLEFINANCE column
    var addr_ticker = getCellAddress(1,2*col +1)
    Sheet.getRange(addr_ticker).setValue(TICKERS[col]);

    // Set the GOOGLEFINANCE column
    var addr = getCellAddress(2,2*col);
    Sheet.getRange(addr).setValue('=GOOGLEFINANCE("'+TICKERS[col]+'", "price", DATE(2014,1,1), DATE(2023, 8, 2), "DAILY")');
  }
}

