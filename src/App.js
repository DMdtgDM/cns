
import EncryptType from "./EncryptType"
import {useState} from "react"

function App() {

  const [algorithm, setAlgorithm] = useState("AES")
  const [encrypted, setEncrypted] = useState("")
  const [decrypted, setDecrypted] = useState("")

  // A function which will handle the click event 
  // Take 3 parameters
  // 1 the key from the input field
  // 2 type: either "encryt" or "decrypt"
  // Text from the textdepending on the type  either to encrypt or decrypt 
  // Ask for a post request to the backing server 
  // Wait on the response 
  // Use the response data for desplay
  async function handleClick(text, key, type) {
      console.log(text + "This is ext", key)
      const response = await fetch(`http://127.0.0.1:5000/${type}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({text: text, key: key, algorithm: algorithm})
      })

      const result = await response.json()
      
      if (result.error) {

        document.querySelector(".alert").innerText = result.e === "ValueError" ? result.error : "Unexpeted Error"
        document.querySelector(".alert").classList.add("error")
          setTimeout(() => {
            document.querySelector(".alert").classList.remove("error");
          }, 2500)
      } else {
        if (type === "encrypt"){
        setEncrypted(result.encrypted_text)
        } else {
          setDecrypted(result.decrypted_data)
        }
      }
      
    
  }


  // Changes the background of the body 
  // Will be applied when the button with class name "bg" is clicked
  const bgChange = () => {
    
    const on = document.querySelector(".bg").classList.contains("on")

    if (on) {
      document.querySelector(".bg").classList.remove("on");
      document.querySelector("body").classList.remove("bgLight");
    } else {
        document.querySelector(".bg").classList.add("on");
        document.querySelector("body").classList.add("bgLight")
      }
   }

  // The following function will copy a given encryption or decryption text
  // Depending on the given parametr which is type
  // also fires an alert message that will flag the copying of the text 
  const copyToClipboard = (type) => {
    let copiedText = type === "encrypt" ? document.querySelector(".encryptedText").value: document.querySelector(".decryptedText").value;
    
     navigator.clipboard.writeText(copiedText)
         .then(() => {
          document.querySelector(".alert").innerText = "Copied to Clipboard !!";
          document.querySelector(".alert").classList.add("appear")
          setTimeout(() => {
            document.querySelector(".alert").classList.remove("appear");
          }, 1500)
          
         })
         .catch(err => {
          console.error("Failed to copy: ", err);
         });
  };



  return (
    <div className="main">
      <button className="bg" onClick={() => {bgChange()}}></button>
      <div className="alert"></div>
      <div className="encrypt">
        <EncryptType type="encrypt" onClick={handleClick} cipher={encrypted} onCopy={copyToClipboard}></EncryptType>
        <EncryptType type="decrypt" onClick={handleClick} cipher={decrypted} onCopy={copyToClipboard}></EncryptType>
      </div>
      <div className="algorihm">
            <button style={{color: "blue"}}>Choose Algorrithm</button>
            <input list="algo" placeholder="Select (default AES)..." onChange={(e) => {setAlgorithm(e.target.value)}}></input>
              <datalist id="algo">
                <option value="OTP" ></option>
                <option value="AES"></option>
                <option value="3DES"></option>
              </datalist>
      </div>
    </div>
  );
}

export default App;
