const MIGRATION_BANNER =
  'Migration candidate generated from the legacy WordPress export';

function plainText(node) {
  if (!node || typeof node !== 'object') return '';
  if (typeof node.value === 'string') return node.value;
  if (!Array.isArray(node.children)) return '';
  return node.children.map(plainText).join('');
}

function cleanChildren(node) {
  if (!node || !Array.isArray(node.children)) return;

  node.children = node.children.filter((child) => {
    if (
      child?.type === 'blockquote' &&
      plainText(child).includes(MIGRATION_BANNER)
    ) {
      return false;
    }

    cleanChildren(child);
    return true;
  });
}

export default function removeMigrationBanner() {
  return (tree) => {
    cleanChildren(tree);
  };
}
