import {useEffect, useRef,useState} from "react"

export default function EncryptType(props) {

  const [encryptKey, setEncryptKey] = useState("");
  const [encryptText, setEncryptText] = useState("");
  const [decryptKey, setDecryptKey] = useState("");
  const [decryptText, setDecryptText] = useState("");



  // This effect will impliment an autofocus when the page is loaded to the ecryption textbox
   const inputRef = useRef(null);
    useEffect(() => {
        
        if (props.type === "encrypt" && inputRef.current) {
            inputRef.current.focus();
        }
    }, [props.type]);


  // A style which changes the color of the text on the buttons
  // Depending on the give the given props type
  // The props is either "decrypt" or "encrypt" 
	const style = {
        color: props.type == "decrypt" ? '#00FF00' : '#FF0000',    
	}

	return (

	<div className="App">
    
      <textarea name="plaintext"  ref={inputRef} onKeyPress={(e)=>{
        props.type == "encrypt" ? setEncryptText(e.target.value + e.key): setDecryptText(e.target.value + e.key)
        console.log(decryptText)
      }} onChange={(e) => {
        console.log(e)
        props.type == "encrypt" ? setEncryptText(e.target.value): setDecryptText(e.target.value)
        console.log(decryptText)}}></textarea>
      <div className="key">
        <button style={style}>{props.type === "decrypt" ? "Decryption Key": "Encryption Key"}</button>
        <input type="text" onKeyPress={(e)=>{props.type == "encrypt" ? setEncryptKey(e.target.value + e.key): setDecryptKey(e.target.value + e.key)}}
        onChange={(e) => {
        props.type == "encrypt" ? setEncryptKey(e.target.value): setDecryptKey(e.target.value)
        }}></input>
      </div>
      <div className="encryption">
        <button className="hover" style={style} onClick={() => {
            const key = props.type === "encrypt" ?  encryptKey: decryptKey
            const text = props.type === "encrypt" ?  encryptText: decryptText
            console.log(text)
            props.onClick(
            text, key, props.type
        )} 
        }>{props.type === "decrypt" ? "Decrypt": "Encrypt"}</button>
        <button className="hover" style={style} onClick={() => {props.onCopy(props.type)}}>{props.type === "decrypt" ? "Copy Decryption": "Copy Encryption"}</button>
      </div>
      <textarea className={props.type == "encrypt" ? "encryptedText": "decryptedText"} value={props.cipher}></textarea>
  </div>

	);
}

