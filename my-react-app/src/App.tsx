import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <Card className="bg-white shadow-lg">
          <CardHeader>
            <CardTitle className="text-2xl">Welcome to My React App</CardTitle>
            <CardDescription>Built with Vite, React, and Tailwind CSS</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <p className="text-gray-600">
                This is a modern React application featuring:
              </p>
              <ul className="list-disc list-inside space-y-2 text-gray-600">
                <li>TypeScript for type safety</li>
                <li>Tailwind CSS for styling</li>
                <li>shadcn/ui components</li>
                <li>Fast development with Vite</li>
              </ul>
              <Button className="mt-4">Get Started</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

export default App
