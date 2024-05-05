import { ThemeProvider } from "@/components/theme-provider";
import { ModeToggle } from "@/components/mode-toggle";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FaqAccordion } from "@/components/FaqAccordion";

function App() {
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
              <Input id="video" type="file" className="w-1/2" />
            </div>
          </div>

          <div className="flex-grow p-4 rounded-lg mb-4 border">
            <Label>Results</Label>

            {/* Display your results here */}
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
