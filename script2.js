
const fs = require('fs');
const path = 'protocol_mayday_presentation_standalone.html';

let content = fs.readFileSync(path, 'utf8');

// 1. Remove the team-overview section
const sectionRegex = /<section id="team-overview" class="slide hero cover-slide" data-slide="01">[\s\S]*?<\/section>/;
content = content.replace(sectionRegex, '');

// 2. Remove the nav link for team-overview
content = content.replace(/\s*<a href="#team-overview">1<\/a>/, '');

// 3. Shift the data-slide indices down by 1 in section attributes
content = content.replace(/data-slide="(\d+)"/g, (match, p1) => {
    let num = parseInt(p1, 10);
    num = num - 1;
    let newStr = num.toString().padStart(2, '0');
    return \data-slide="\"\;
});

// 4. Update total slide count in CSS
content = content.replace('content: attr(data-slide) " / 11";', 'content: attr(data-slide) " / 10";');

// 5. Shift nav links numbers down by 1
content = content.replace(/<a href="([^"]+)">(\d+)<\/a>/g, (match, href, numStr) => {
    let num = parseInt(numStr, 10);
    num = num - 1;
    return \<a href="\">\<\/a>\;
});

// 6. Update the brand link href
content = content.replace('<a class="brand" href="#team-overview"', '<a class="brand" href="#project-title"');

fs.writeFileSync(path, content, 'utf8');
console.log('Done');

