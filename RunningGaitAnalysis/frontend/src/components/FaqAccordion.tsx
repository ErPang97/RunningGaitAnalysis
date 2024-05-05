import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

export function FaqAccordion() {
  return (
    <Accordion type="single" collapsible className="w-full">
      <AccordionItem value="item-1">
        <AccordionTrigger>How does this work?</AccordionTrigger>
        <AccordionContent>
          <p>• In order to analyze your running gait, first, attach a video in `mp4` format. </p>
          <p>• Taking videos from a treadmill from a sideways view is the most ideal for processing data. </p>
          <p>• After attaching the video, click "Run Analysis" to get insights on your running form!</p>
        </AccordionContent>
      </AccordionItem>
      <AccordionItem value="item-2">
        <AccordionTrigger>What is the criteria for evaluating my running form?</AccordionTrigger>
        <AccordionContent>
          <p>• Running form is evaluated based on various biomechanical criteria based of research. Please note that although research has provided generalizations for optimal running, running is a unique and personalized movement!</p>
          <p>• Davis, S. (2016). Running Atlas: A Literature Review of Running Form and Technique, The. <a href="https://uwyo.figshare.com/articles/thesis/Running_Atlas_A_Literature_Review_of_Running_Form_and_Technique_The/13699741" className="text-sky-400">Link</a></p>
          <p>• Michaud, T. C. (2016). Should you change an athlete's natural running form?. AMAA Journal, 29(3), 11-14. <a href="https://go.gale.com/ps/i.do?id=GALE%7CA477991577&sid=googleScholar&v=2.1&it=r&linkaccess=abs&issn=&p=AONE&sw=w&userGroupName=anon%7Ef6e1c0e6&aty=open-web-entry" className="text-sky-400">Link</a></p>
        </AccordionContent>
      </AccordionItem>
      <AccordionItem value="item-3">
        <AccordionTrigger>Why should I care about my running form?</AccordionTrigger>
        <AccordionContent>
          <p>There are numerous benefits to improving your running form!</p>
          <p>• <b>Efficiency</b>: Proper running form helps you move more efficiently, allowing you to cover more distance with less effort.</p>
          <p>• <b>Injury Prevention</b>: Good form reduces the risk of common running injuries by minimizing stress on joints and muscles.</p>
          <p>• <b>Performance Improvement</b>: Optimizing your form can lead to better race times and overall performance enhancement.</p>
          <p>• <b>Energy Conservation</b>: By running with good form, you use less energy, enabling you to run longer distances without fatigue.</p>
          <p>• <b>Balance and Stability</b>: Maintaining proper form enhances your balance and stability, reducing the likelihood of falls or trips.</p>
          <p>• <b>Long-Term Health</b>: Consistently practicing good form promotes long-term joint health and overall well-being.</p>
          <p>• <b>Biofeedback</b>: Paying attention to your form provides valuable feedback about your body's mechanics and areas for improvement.</p>
          <p>• <b>Mind-Body Connection</b>: Focusing on form cultivates mindfulness and a deeper connection between your body and mind during running.</p>
        </AccordionContent>
      </AccordionItem>
    </Accordion>
  )
}
