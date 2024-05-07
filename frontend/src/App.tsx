import { useState } from 'react'
import axios from 'axios'
import { ThemeProvider } from "@/components/theme-provider";
import { ModeToggle } from "@/components/mode-toggle";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FaqAccordion } from "@/components/FaqAccordion";
import { Button } from "./components/ui/button";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:5000/uploadVideo', formData, {
      // await axios.post('uploadVideo', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      // Handle success, e.g., show a success message

      const responseData = response.data

      if (responseData.error) {
        console.error('Server error:', responseData.error)
        alert('Server error: ' + responseData.error)
        return
      }

      setResult(responseData)
      
      alert('File uploaded successfully');
    } catch (error) {
      // Handle error, e.g., show an error message
      console.error('Error uploading file:', error);
      alert('Error uploading file. Please try again.');
    }
  };

  console.log(result)

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="flex flex-col min-h-screen">
        <div className="container mx-auto px-4 py-8 flex-grow flex flex-col">
          <div className="flex justify-between mb-4">
            <h1 className="text-2xl font-bold mb-4">Running Gait Analysis</h1>
            <ModeToggle />
          </div>


          <div className="mb-4">
            <Label htmlFor="video" className="block mb-2">Attach Video</Label>
            <div className="max-w-lg">
              <Input id="video" type="file" className="w-1/2" onChange={handleFileChange}/>
            </div>
          </div>

          <Button className="mb-4 max-w-64" variant="secondary" onClick={handleSubmit}>Get Your Analysis</Button>
        

          <div className="flex-grow p-4 rounded-lg mb-4 border">
            <Label>Results</Label>
            {result &&
              <p1>Right Arm Angle Difference: </p1>
            }

          </div>
        </div>

        <div className="container py-10">
          <h2>FAQs</h2>
          <FaqAccordion />
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
