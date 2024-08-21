import styles from "./Modal.module.css";

interface IModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export function Modal({ isOpen, onClose, children }: IModalProps) {
  if (!isOpen) return null;

  return (
    <div className={styles.backdrop} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <form>
          <label>
            Input:
            <input
              type="datetime-local"
              name="input"
              defaultValue={new Date().toISOString().slice(0, 16)}
              required
              style={{ border: "1px solid black" }}
            />
          </label>
        </form>
        <button className={styles.closeButton} onClick={onClose}>
          X
        </button>
        {children}
      </div>
    </div>
  );
}
