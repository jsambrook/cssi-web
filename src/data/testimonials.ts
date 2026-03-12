import type { Testimonial } from './types';

export const testimonials: Testimonial[] = [
  {
    quote:
      'I brought John Sambrook onto a risky and highly political project that had far-reaching consequences within our company. As the second software engineer on the team, me being the first, John found solutions to difficult problems, problems I could not have solved without him, thwarting doom over and over again. He produced documentation and code at a professional level I have rarely seen elsewhere in my thirty years of software engineering. The project was so successful, the team was spun off as its own company, which now employs 700 people.',
    name: 'Bob Alexander',
    title: 'Principal Software Architect',
    company: 'Fujifilm Sonosite',
  },
  {
    quote:
      "I've run enough companies to know the difference between \"competitive\" and unfair. At Applied Microsystems, we had an unfair advantage—and one of the clearest examples came from John Sambrook and the outstanding engineers he assembled and led.\n\nJohn's group built our symbolic debugger and intelligent trace disassembler. Other tools could show you pieces—addresses, disassembly, maybe a shaky stack trace. John's team built a reconstruction engine that turned raw trace data into a coherent, source-correlated story of what the target processor actually did, even with interrupts, optimized code, and messy control flow.\n\nHewlett-Packard was a giant competitor—great people, huge resources—but that kind of deep, reality-faithful tooling is hard for big organizations to justify and harder to execute. HP could sell tools. We could deliver the truth. And customers felt that immediately when they hit the hard bugs.",
    name: 'Bob Deinhammer',
    title: 'CEO',
    company: 'Applied Microsystems',
  },
];
