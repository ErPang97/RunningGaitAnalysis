import { ThemeProvider } from "@/components/theme-provider";
import { ModeToggle } from "@/components/mode-toggle";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="container mx-auto px-4 py-8">
        <div className="flex justify-between mb-4">
          <h1 className="text-2xl font-bold mb-4">Running Gait Analysis</h1>
          <ModeToggle />
        </div>

        <div className="mb-4">
          <Label htmlFor="video" className="block mb-2">Attach Video</Label>
          <div className="max-w-lg">
            <Input id="video" type="file" className="w-1/2"/>
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
